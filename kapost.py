# import boto3
# import os
# s3 = boto3.resource('s3')
# first_bucket = s3.Bucket('177621984')
# second_bucket = s3.Bucket('198421776')


import boto3
s3 = boto3.resource('s3')
bucket_1 = s3.Bucket('177621984')
bucket_2 = s3.Bucket('198421776')
threshold = 1000


def filter_by_threshold(bucket_1, bucket_2, threshold):
    for o in bucket_1.objects.all():
        if (o.size > threshold) in o.key:
            print (copy_source = {
            'Bucket': bucket_1,
            'Key': o.key
            })
        s3.meta.client.copy(copy_source, 'bucket_2', 'otherkey')


filter_by_threshold(bucket_1, bucket_2, threshold)


#Create Conditional That Filters Out Files Less Than Threshhold
# if (bucket.size > threshold)
# copy_source = {
#     'Bucket': first_bucket,
#     'Key': 'mykey'
# }
# s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')


# import boto

# c = boto.connect_s3()
# src = c.get_bucket('my_source_bucket')
# dst = c.get_bucket('my_destination_bucket')

# for k in src.list():
#     # copy stuff to your destination here
#     dst.copy_key(k.key.name, src.name, k.key.name)
#     # then delete the source key
#     k.delete()
