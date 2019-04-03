import pdb
import argparse
import boto3
import sys


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
            copy_source = {
            'Bucket': o.bucket_name,
            'Key': o.key
            }
            dst_bucket.copy(copy_source, o.key)
    

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

main(sys.argv[1:])
