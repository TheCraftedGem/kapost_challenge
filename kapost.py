# import boto3
# s3 = boto3.resource('s3')

#Create Conditional That Filters Out Files Less Than Threshhold

# copy_source = {
#     'Bucket': 'mybucket',
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
