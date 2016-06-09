function [ v r ] = CryptoECisValid( A, B, p )

    r = mod(4*A^3 + 27*B^2, p);
    if r ~= 0
        v = 1;
    else
        v = 0;
    end
    
end

