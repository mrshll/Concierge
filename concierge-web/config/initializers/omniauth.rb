Rails.application.config.middleware.use OmniAuth::Builder do
  provider :singly, ENV['SINGLY_ID'], ENV['SINGLY_SECRET']
end
