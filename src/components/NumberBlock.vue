<template>
    <div
        class="border-l border-t border-yellow-400 w-16 h-10 flex items-center justify-center font-serif text-2xl font-extrabold"
        :class="[
                            color, 
                        number.number % 3 === 0 ? 'border-r' : '',
                        number.number > 33 ? '' : '',
                        isActive ? 'bg-green-800' : ''
                        ]"
       
       
    >
        {{ number.number }}
    </div>
</template>

<script setup>
import RouletteNumbers from '../src/RouletteNumbers.js'
import { computed } from 'vue'

const props = defineProps(["number","bet"])

const color = computed(() => {
    return {
        "red": "text-[#D00000]",
        "black": "text-black",
        "green": "text-yellow-300"
    }[props.number["color"]]
})


const isActive = computed(() => {
    
    if(props.bet?.type !== "Number") {
        return false
    }
    return props.bet.value === props.number.number
})






</script>


<style scoped>

</style>
