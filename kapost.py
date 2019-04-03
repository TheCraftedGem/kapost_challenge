import argparse
import boto3

#Copies Files From Source Bucket To Destination Bucket If Filesize Is Over Threshold
def main(argv):
    args = cli(argv)
    src = args.src
    dst = args.dst
    threshold = args.size

    s3 = boto3.resource('s3')

    src_bucket = s3.Bucket(src)
    dst_bucket = s3.Bucket(dst)

    for o in src_bucket.objects.all():
        if (o.size / (2 ** 20)) > threshold:
            source = {
            'Bucket': src_bucket,
            'Key': o.key
            }
            dst_bucket.copy(source, o.key)
    
#Creates CLI Argument Parser For Main Function
def cli(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--from", dest="src", type=str, required=True
    )
    parser.add_argument(
        "-t", "--to", dest="dst", type=str, required=True
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        required=True,
    )
    return parser.parse_args(argv)