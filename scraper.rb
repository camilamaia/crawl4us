require 'rubygems'
require 'nokogiri'
require 'open-uri'

PAGE_URL = ""

page = Nokogiri::HTML(open(PAGE_URL))

assets = []
page.css('tr').each do |tr|
  asset = []
  tr.css('td').each do |td|
    asset << td.text.strip
  end
  assets << asset
end
