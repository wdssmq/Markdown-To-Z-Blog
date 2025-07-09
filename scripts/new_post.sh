#!/bin/bash

cd _posts
_date=$(date +%Y-%m-%d)
_datetime=$(date +%Y-%m-%d\ %H:%M:%S)
_empty=1970-01-01-empty.md

# 处理已存在的目录，重命名并更新其中的日期
if [ -d *-new-post ]; then
  mv *-new-post "${_date}-new-post"
  if [ -f "${_date}-new-post/doc.md" ]; then
    sed -i "s/date: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]/date: ${_datetime}/" "${_date}-new-post/doc.md"
  fi
fi

# 处理已存在的文件，重命名并更新其中的日期
if [ -f *-new-post.md ]; then
  mv *-new-post.md "${_date}-new-post.md"
  sed -i "s/date: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]/date: ${_datetime}/" "${_date}-new-post.md"
fi

if [ ! -f "${_date}-new-post.md" ]; then
  cp "${_empty}" "${_date}-new-post.md"
  sed -i "s/{{ date }}/${_datetime}/" "${_date}-new-post.md"
fi

if [ ! -d "${_date}-new-post" ]; then
  mkdir "${_date}-new-post"
  cp "${_empty}" "${_date}-new-post/doc.md"
  sed -i "s/{{ date }}/${_datetime}/" "${_date}-new-post/doc.md"
fi

code "${_date}-new-post.md"
