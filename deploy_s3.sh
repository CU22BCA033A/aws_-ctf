#!/bin/bash

BUCKET="my-ctf-competition"
aws s3 cp challenge1_source.html s3://$BUCKET/ --acl public-read
aws s3 cp challenge2_cookie.html s3://$BUCKET/ --acl public-read
aws s3 cp challenge3_script.html s3://$BUCKET/ --acl public-read
aws s3 cp style.css s3://$BUCKET/ --acl public-read

echo "URLs:"
echo "https://$BUCKET.s3-website-<region>.amazonaws.com/challenge1_source.html"
echo "https://$BUCKET.s3-website-<region>.amazonaws.com/challenge2_cookie.html"
echo "https://$BUCKET.s3-website-<region>.amazonaws.com/challenge3_script.html"
