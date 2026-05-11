<template>
    <div
        class=" border-b border-yellow-400 w-15 h-40 flex items-center justify-center text-yellow-300  font-serif text-2xl">
        <div class="[writing-mode:vertical-lr]">
            {{dozen}}<span class="text-lg">{{ suffix }}</span> 12
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps(["dozen"])

const suffix = computed(() => {
   return  {
        1: 'st',
        2: 'nd',
        3: 'rd'
    }[props.dozen]
})

</script>


