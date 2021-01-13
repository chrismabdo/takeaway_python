class CountApp < Sinatra::Base
    enable :sessions

    get '/' do
        erb :home
    end

    get 'count' do
        count = session[:count] || 0.to_s
    end





end