#!/bin/bash
lftp -u iopsn2290,iopsn2290Pomp_2018#EuoP sftp://10.14.15.18:22 <<EOF
chmod -R 775 /data/2290/activity/$(date +%Y%m%d)
bye
EOF

lftp -u iophn2731,iophn2731_Pomp_2018#EuoP sftp://10.14.15.18:22 <<EOF
chmod -R 775 /data/2731/activity/$(date +%Y%m%d)
bye
EOF