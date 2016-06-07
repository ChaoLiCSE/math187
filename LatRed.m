function [ v1 ] = LatRed( v1, v2 )
% Lattice Reduction
% 1. If ?v1? > ?v2?, swap v1 and v2 so that ?v1? ? ?v2?.
% 2. Let t be the closest integer to (v1 • v2)/(v1 • v1).
% 3. If t = 0, stop. If t ? 0, replace v2 by (v2 - tv1) and go to step 1

    t = 1;
    iter = 0;
    
    fprintf('iter v1 v2 n1 n2 swap u t\n')
    while t ~= 0
        n1 = norm(v1);
        n2 = norm(v2);
        fprintf('%d  [%.3f, %.3f]  [%.3f, %.3f]  %.3f  %.3f  ', iter, v1, v2, n1, n2);
        
        if n2 < n1
            tmp = v1;
            v1 = v2;
            v2 = tmp;
            fprintf('yes  ');
        else
            fprintf('no  ');
        end 
        
        u = dot(v1, v2)/dot(v1,v1);
        t = round(u);
        
        fprintf('%.3f   %d\n', u, t)
        v2 = v2 - t*v1;
        iter = iter + 1;
    end
    
    


end

