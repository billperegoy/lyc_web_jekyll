#!/usr/bin/ruby

require 'time'
require "yaml"

def print_single_day_classes(classes, day)
  classes[day].each do |cl|
    # puts "#{day} #{cl['time']}   #{cl['type']}  #{cl['teacher']}  #{cl['duration']}"
    puts "<tr class=\"#{day}\"><td>#{day.capitalize}</td><td>#{cl['time']}</td><td>#{cl['type']}</td><td>#{cl['teacher']}</td><td>#{cl['duration']} min</td></tr>"
  end
end

def print_schedule_header
  puts "<div class=\"schedtable\">"
  puts "<table>"
  puts "<tr class=\"schedhead\"><th>Day</th><th>Time</th><th>Class Type</th><th>Teacher</th><th>Length</th></tr>"
end

def print_schedule_footer
  puts "</table>"
  puts "</div>"
end


puts "Content-type: text/html\n\n"

ruby_obj = YAML.load_file('schedule.yml')
classes = ruby_obj['classes']

print_schedule_header
print_single_day_classes(classes, 'sunday')
print_single_day_classes(classes, 'monday')
print_single_day_classes(classes, 'tuesday')
print_single_day_classes(classes, 'wednesday')
print_single_day_classes(classes, 'thursday')
print_single_day_classes(classes, 'friday')
print_single_day_classes(classes, 'saturday')
print_schedule_footer

