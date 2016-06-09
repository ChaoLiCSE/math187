function [ P ] = CryptoNegP( P, p )

    n = -mod(P(1,2) , p);
    
    if n < 0
        n = mod(n, p); 
    end

    P = [P(1,1), n];
end

