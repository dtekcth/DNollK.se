xml.instruct! :xml, :version => "1.0"
xml.rss :version => "2.0" do
  xml.channel do
    xml.title #{Config::SITE_TITLE}
    xml.description #{Config::RSS_DESCRIPTION}
    xml.link request.url.chomp request.path_info

    @news.each do |newsitem|
      xml.item do
        xml.title newsitem.heading.gsub(/_/, " ")
        xml.link "#{request.url.chomp request.path_info}/#{newsitem.id}"
        xml.guid "#{request.url.chomp request.path_info}/#{newsitem.id}"
        xml.pubDate Time.parse(newsitem.date.to_s).rfc822
        xml.description newsitem.data
      end
    end
  end
end
