task :default => :all

task :all => [:build, :push]

task :build => [:run_jekyll, :fix_posts]

task :run_jekyll do
  sh 'jekyll build'
  sh 'chmod +x _site/cgi-bin/*.cgi'
end

task :fix_posts do
  puts "Fixing posts"
  dir_list = Dir.glob("_site/**/*.html").each do |old_file|
    new_file = old_file.sub(/html$/, 'shtml' )
    File.rename(old_file, new_file)
  end
  
  ## Need to change all the posts from index.html to index.shtml
  #fix_posts:
  #	for fn in `find _site/jekyll -name index.html -print` 
  #	do 
  #	  echo "Got: $fn" 
  #	done
end

task :push do
  sh 'rsync -rp _site/* peregoy@lawrenceyoga.com:/home/peregoy/lawrenceyoga.com'
  sh 'rsync -p _site/.htaccess peregoy@lawrenceyoga.com:/home/peregoy/lawrenceyoga.com'
end
