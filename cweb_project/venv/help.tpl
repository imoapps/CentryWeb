<ul>
% for item in basket:
    <li>{{item}}</li>
    %end
    </ul>
    <div>
    % if True:
        </div>
        this renders to clean html
        <div>
        <span>content</span>
        </div>
        <div>\\
%if True:
<span>content</span>\\
%end
</div>
