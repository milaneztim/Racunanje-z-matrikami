% rebase('osnova.tpl')


<h2>Vnesite elemente matrike:</h2>
<form action="/dodaj-matriko/{{ime_matrike}}" method="POST" class="matrika">
	% for i in range(m):
		<div class="vrstica">
			% for j in range(n):
				<input type="number" step="any" class="element" placeholder="0" name="{{i}}x{{j}}">
			% end
		</div>
	% end
	<input type="submit" value="Shrani matriko" class="matrika">
</form>
