<script>
    import { onMount } from 'svelte';
      // globs
    let WORD_AMT = 25;
    const back_domain = "http://localhost:8000";
    let word_bank = [];

    console.log("innitalizing word bank");

    onMount(async () => {
        console.log(`Mounting dom`)
        console.log(WORD_AMT)
        // word_bank = get_words(WORD_AMT)
    });

    function handle_keypress(event){
        pass
    }

    async function get_words(bank_size){
        const params = {
            size: bank_size
        };

        const queryString = Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&');
       
        const url = `${back_domain}/getWords?${queryString}`;

        fetch(url)
            .then(response => {
            if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
            }
            return response.json();
            })
            .then(data => {
            console.log(data);
            })
            .catch(error => {
            console.error('Error:', error);
            });
    }
    console.log(word_bank);

</script>

<button on:click(add1)>
    append
</button>
<h1>
    {test}
</h1>






<p>
    {word_bank[1]}
    {word_bank[2]}
    {word_bank[3]}
    {word_bank[4]}
</p>
    
