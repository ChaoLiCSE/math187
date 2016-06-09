function [ r ] = LatIsReduced( v1, v2 )

    display('test cond 1;');
    v1norm = norm(v1)
    v2norm = norm(v2)
    if v1norm > v2norm
        r = 0;
        return;
    end
    
    display('test cond 2:');
    top = dot(v1, v2)
    bot = dot(v1, v1)
    if (-1/2) >= top/bot || top/bot >= 1/2
        r = 0;
        return;
    end
    
    r = 1;
end

