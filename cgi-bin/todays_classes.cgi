#!/usr/bin/ruby

require 'time'
require "yaml"

def day_to_str(day)
  days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
  return days[day]
end

day = Time.now.wday
day_str = day_to_str(day)

ruby_obj = YAML.load_file('schedule.yml')
classes = ruby_obj['classes']

daily_classes = classes[day_str]
puts "Content-type: text/html\n\n"

if daily_classes
  daily_classes.each do |cl|
    puts "#{cl['time']}<br/>"
  end
else
  puts "No classes today<br/>"
end



