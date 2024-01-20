<script>
	import reload_img from "$lib/imgs/reload_keys_symbol.png"

	import logo from "$lib/imgs/winston.jpg"

</script>



<h1>
	<img src={logo} alt = "wynton"/>
	TypingTest
	<span>
		<button>
			<img src={reload_img} alt="reload img"
			width = 30/>
		</button>
	</span>
</h1>
<!-- need to make button transparent later -->

<style>
	h1{
		color: rgb(139, 59, 59);
		font-family: 'Gotham';
		font-size: 1.75em;
		font-weight: 600;
	}

	:global(body) { 
		background-color: rgb(41, 35, 36);
  }

  
  
</style>

