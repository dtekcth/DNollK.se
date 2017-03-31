# coding: utf-8

require 'sinatra'

class DNollKApp::Routes < Sinatra::Application
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
  
  get '/rss.xml' do
    @news = News.all :order => :date.desc
    builder :rss
  end
end
