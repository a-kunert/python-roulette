<template>
    <div
        class="w-15 h-40 flex items-center justify-center text-yellow-300  font-serif text-2xl"
        :class="dozen !== 3 ? 'border-b border-yellow-400' : 'border-yellow-400'"

    >
        <div class="[writing-mode:vertical-lr]">
            {{dozen}}<span class="text-lg">{{ suffix }}</span> 12
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  dozen: Number,
  setBet: Function
})

const suffix = computed(() => {
   return  {
        1: 'st',
        2: 'nd',
        3: 'rd'
    }[props.dozen]
})

</script>


