#!/bin/bash

cd _posts
_date=$(date +%Y-%m-%d)
_empty=1970-01-01-empty.md

if [ -d *-new-post ]; then mv *-new-post "${_date}-new-post"; fi
if [ -f *-new-post.md ]; then mv *-new-post.md "${_date}-new-post.md"; fi

if [ ! -f "${_date}-new-post.md" ]; then
  cp "${_empty}" "${_date}-new-post.md"
  sed -i "s/{{ date }}/$(date +%Y-%m-%d\ %H:%M:%S)/" "${_date}-new-post.md"
fi

if [ ! -d "${_date}-new-post" ]; then
  mkdir "${_date}-new-post"
  cp "${_empty}" "${_date}-new-post/doc.md"
  sed -i "s/{{ date }}/$(date +%Y-%m-%d\ %H:%M:%S)/" "${_date}-new-post/doc.md"
fi

code "${_date}-new-post.md"
