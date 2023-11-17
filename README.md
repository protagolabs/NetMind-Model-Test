<h1 align="center">NetMind-Model-test</h1>
<p align="center">
NetMind-Model-Test
</p>

## Overview
This repo used to record code for model testing in multi platform such as windows or linux.


google test doc link : https://docs.google.com/spreadsheets/d/1Gco984a4gZqg9rOT0NO3i3BgKgdYpsObOipHWOzmo1I/edit#gid=0

## Structure

Table below shows model name and train arguments.
Datasets stored in s3
https://s3.console.aws.amazon.com/s3/buckets/protagolabs-netmind-datasets-test?region=us-west-2&prefix=model_test

| directory name                  | model_name | dataset_name                 | train_batch_size | total_step |
|---------------------------------| ---------- |------------------------------|------------------|------|
| albert-base-v2                  | albert-base-v2 | albert_tokennized_wikitext.tar.gz   | 8                | 5000 |
| bert-large-uncased              | bert-large-uncased | albert_tokennized_wikitext.tar.gz   | 4                | 1000 |
| gpt2-large                      | gpt2-large | gpt2_data.tar.gz             | 4                | 2334 |
| resnet101                       | resnet101 | tiny-imagenet-200.tar.gz     | 128              | 35190 |
| stable-diffusion-xl             | stable-diffusion-xl-base-1.0 | dataset specified in train code | 1                | 1251 |


