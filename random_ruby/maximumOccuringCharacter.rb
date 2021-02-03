def maximumOccurringCharacter(text)
    # Write your code here
    characterOccurence = {
        
    }
    
    text.each_char do |char, idx|
        if(characterOccurence.has_key?(char))
           characterOccurence[char] += 1
        else
            characterOccurence[char] = 1 
        end
    end
    
    mostOccuringCharacter = nil
    characterOccurence.each_pair do |key, value|
        if !mostOccuringCharacter
           mostOccuringCharacter = key
        elsif value > characterOccurence[mostOccuringCharacter]
            mostOccuringCharacter = key
        end
    end
    
    return mostOccuringCharacter
end