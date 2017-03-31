# coding: utf-8
require 'sinatra/base'
require 'sinatra/flash'
require 'data_mapper'
require 'builder'

require './app/config'

DataMapper::setup(:default, "mysql://#{Config::USER[:name]}:#{Config::USER[:password]}@#{Config::DATABASE[:host]}/#{Config::DATABASE[:db]}")

DataMapper.finalize.auto_upgrade!

class DNollKApp < Sinatra::Base

  enable :sessions
  register Sinatra::Flash

  helpers do
    include Rack::Utils
    alias_method :h, :escape_html
  end
  
  get '/' do
    if Config.const_defined? "DEFAULT_ROUTE"
      redirect Config::DEFAULT_ROUTE
    else
      "Home page for #{Config::SITE_TITLE}"
    end
  end

  get '/news' do
    @news = News.all :order => :date.desc
    if @news.empty?
      flash[:notice] = "Här var det tomt, Mottagningen #{Time.now.year} har kanske inte börjat än."
    end
    erb :news
  end

  get '/news/:id' do
    @news = News.get params[:id]
    erb :one_news
  end
  
  get '/rss.xml' do
    @news = News.all :order => :date.desc
    builder :rss
  end
end
