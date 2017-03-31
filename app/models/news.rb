class News
  include DataMapper::Resource
  property :id, Serial
  property :heading, Text
  property :snippet, Text
  property :data, Text
  property :date, DateTime
  property :published, Boolean, :required => true, :default => false
end

