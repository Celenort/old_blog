git pull
python3 scripts/update_visitors.py
rm -rf ./_site
bundle exec jekyll clean
bundle exec jekyll build
pkill -9 nginx
nginx -p $CONDA_PREFIX/etc/nginx -c $CONDA_PREFIX/etc/nginx/nginx.conf
