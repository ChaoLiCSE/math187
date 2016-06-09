function [ v r ] = ECisValid( A, B )

    r = 4*A^3 + 27*B; 
    if  r ~= 0
        v = 1;
    else
        v = 0;
    end


end

