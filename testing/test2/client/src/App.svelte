<script>
//	import Buttom from "./Button.svelte"

	data = "21 savage"

	function sayHello(){
	fetch("/data")
	.then(d => d.text())
	.then(d => (data = d));
	}	
</script>


<h1>
fuck you bitch
</h1>


<Button class = "dataGetter" on:click{sayHello}>
	getData
</Button>
