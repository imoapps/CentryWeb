<h1> Incomming Transactions </h1>
<table>
<tr><th>Id  </th><th> Date  </th><th>  Agent  </th><th>Ref.No</th><th>Amount</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
