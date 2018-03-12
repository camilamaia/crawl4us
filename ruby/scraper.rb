require 'rubygems'
require 'nokogiri'
require 'open-uri'

ADM = ['administradora', 'admin', 'adm', 'admin.']
CRE = ['crédito', 'credito']
ENT = ['entrada']
SAL = ['saldo']
COM = ['complemento']
OBS = ['observações', 'observacoes', 'observaçoes', 'observacões', 'obs']
SIT = ['situação', 'situacao', 'situaçao', 'situacão']

PAGE_URL = ''

def map_columns_names header
  header.map do |col|
    if ADM.include? col
      'adm'
    elsif CRE.include? col
      'crédito'
    elsif ENT.include? col
      'entrada'
    elsif SAL.include? col
      'saldo'
    elsif COM.include? col
      'complemento'
    elsif OBS.include? col
      'observações'
    elsif SIT.include? col
      'situação'
    else
      '--'
    end
  end
end

def scrap_data
  page = Nokogiri::HTML(open(PAGE_URL))

  assets = []
  page.css('tr').each do |tr|
    asset = []
    tr.css('td').each do |td|
      asset << td.text.strip
    end
    assets << asset
  end

  return assets
end


assets = scrap_data
assets.reject! {|a| a.size != 6}
header = assets.shift.map {|h| h.downcase}
map_columns_names header
