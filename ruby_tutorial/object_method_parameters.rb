class Integer

    def range?(b, c)
        return self >= b && self <= c
    end
end

puts 10.range?(1, 11)
puts 10.range?(11, 100)