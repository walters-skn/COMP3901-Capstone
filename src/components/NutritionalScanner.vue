

<template> 
    <p class="error">{{ error }}</p>
    <p> {{ decodedString }}</p>
    <qrcode-stream @init="onInit" @decode="onDecode"></qrcode-stream>
</template>


<script>

import {QrcodeStream} from 'vue3-qrcode-reader'

export default{
    data(){
        return{
            error: '',
            decodedString: '',
        }
    },
    components:{
        QrcodeStream
    },
    methods: {
        async onInit(promise){
            try {
                await promise
            } catch (error) {
                if (error.name === 'NotAllowedError') {
                this.error = "ERROR: you need to grant camera access permission"
                } else if (error.name === 'NotFoundError') {
                this.error = "ERROR: no camera on this device"
                } else if (error.name === 'NotSupportedError') {
                this.error = "ERROR: secure context required (HTTPS, localhost)"
                } else if (error.name === 'NotReadableError') {
                this.error = "ERROR: is the camera already in use?"
                } else if (error.name === 'OverconstrainedError') {
                this.error = "ERROR: installed cameras are not suitable"
                } else if (error.name === 'StreamApiNotSupportedError') {
                this.error = "ERROR: Stream API is not supported in this browser"
                }
                this.error = `ERROR: Camera error (${error.name})`;
                }
            },
            onDecode(decodedString){
                //this.decodedString = decodedString;
                window.location.replace(decodedString)

            }
        }
}

</script>

<style scoped> 
.error {
  font-weight: bold;
  color: red;
}

</style>