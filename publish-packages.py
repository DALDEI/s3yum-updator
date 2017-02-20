#!/usr/bin/env python
"""Script to upload packages to s3 and notify repoupdate-daemon."""
import os
import optparse
import boto
import boto.sns

parser = optparse.OptionParser()
parser.add_option('--bucket', default='marklogic-qa-build-yumrepo')
parser.add_option('--repopath', default='x86_64')
parser.add_option('--region', default='us-west-2')
parser.add_option('--sns-topic', default='arn:aws:sns:us-west-2:027394069461:packages-new')
options, args = parser.parse_args()

sns = boto.sns.connect_to_region(options.region)
bucket = boto.connect_s3().get_bucket(options.bucket, validate=False)
for rpmfile in args:
    filename = os.path.split(rpmfile)[1]
    """key = bucket.new_key(os.path.join(options.repopath, filename))
    key.set_contents_from_filename(rpmfile) """
    sns.publish(options.sns_topic, filename, options.repopath)
