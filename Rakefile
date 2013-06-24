task :default => :all

task :all => [:build, :push]

task :build => [:run_jekyll, :fix_posts]

task :run_jekyll do
  puts "Running jekyll"
  sh 'jekyll build'
  sh 'chmod +x _site/cgi-bin/*.cgi'
end

task :fix_posts do
  puts "Fixing posts"
  dir_list = Dir.glob("_site/**/*.html").each do |old_file|
    new_file = old_file.sub(/html$/, 'shtml' )
    File.rename(old_file, new_file)
  end
end

task :push do
  puts "Pushing site to server"
  sh 'rsync -rp _site/* peregoy@lawrenceyoga.com:/home/peregoy/lawrenceyoga.com'
  sh 'rsync -p _site/.htaccess peregoy@lawrenceyoga.com:/home/peregoy/lawrenceyoga.com'
end
