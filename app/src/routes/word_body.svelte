<script>
    import { onMount } from 'svelte';
      // globs
    let word_amount = 25;
    const back_domain = "http://localhost:8000";
    let word_bank = [1,1,1,1,1];
    console.log("innitalizing word bank");

    onMount(async () => {
        console.log(`Mounting dom`)
        console.log(word_amount)
        word_bank = get_words(word_amount)
    });

    function handle_keypress(event){
        pass
    }
//
    function get_words(bank_size){

        let url = back_domain + "/getWords"
        // url = url + new URLSearchParams({
        //     size:bank_size
        // });
        
        //requesting from backend
        fetch(back_domain + "/getWords",
        )
        .then(response => word_bank)
        .catch(error => console.error('Error: ',error))
    }
// 
</script>


<p>
    {word_bank[1]}
    {word_bank[2]}
    {word_bank[3]}
    {word_bank[4]}
</p>