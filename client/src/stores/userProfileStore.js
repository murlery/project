import axios from "axios";
import { defineStore} from "pinia"; 
import { onBeforeMount } from "vue";


const useUserProfileStore=defineStore("UserProfileStore",()=>{
    const is_auth = ref();
    const username = ref();
    const is_superuser = ref();

    onBeforeMount(()=>{
        const v = axios.get("user/info")
        is_auth.value = r.data.is_auth
        username.value = r.data.name

    })
    return{is_auth,username,is_superuser}
})
export default useUserProfileStore;