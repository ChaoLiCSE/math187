function [ xInv ] = modInv(n, p)
% ModInv(x,n) computes the multiplicative inverse of x modulo n if one
%   exists; errors if no such inverse exists
    if gcd(n,p) ~= 1
        error('x has no inverse modulo n')
    end

    [d, a, b]   = gcd(n,p);
    xInv        = mod(a,p);
end

