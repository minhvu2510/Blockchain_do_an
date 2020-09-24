<template>
    <div>
        <el-row :gutter="12" style="padding-top: 15px">
            <el-col :span="7">
                <br/>
            </el-col>
            <el-col :span="10">
                <el-card shadow="always">

                    <div>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="18" style="text-align: left">
                                <strong>Bài thi đã kết thúc, hệ thống sẽ tự thoát sau {{dem}} s</strong>
                                <!--<el-checkbox v-model="checked">Đã xác nhận thông tin!</el-checkbox>-->
                                <!--<span style="color: #9a9e9f">Xác nhận lại thông tin!</span>-->
                            </el-col>
                            <el-col :span="2">
                                <br/>
                            </el-col>

                        </el-row>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="18" style="text-align: left">
                                <!--<strong>Điểm sẽ được gửi qua mail khi có kết quả</strong>-->
                                <!--<el-checkbox v-model="checked">Đã xác nhận thông tin!</el-checkbox>-->
                                <!--<span style="color: #9a9e9f">Xác nhận lại thông tin!</span>-->
                            </el-col>
                            <el-col :span="2">
                                <br/>
                            </el-col>

                        </el-row>


                    </div>
                </el-card>
            </el-col>
            <el-col :span="7">
                <br/>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import { notify } from '@/api/questions'
    export default {
        name: "end",
        data() {
            return {
                dem: 5
            }
        },
        mounted () {
            // this.myFuntion()
            // this.$router.push('/confirm')
            this.logout()
        },

        methods: {
            myFuntion() {
                setInterval(function(){
                    console.log('00000')
                    var k = Number(this.dem)
                    this.dem = 4
                    console.log('00000',typeof ( this.dem))
                    console.log('00000', Number(this.dem))
                    if (this.dem > 0){
                        var k = Number(this.dem)
                        this.dem = k - 1
                    }
                }, 1000);
            },
            logout() {
                setTimeout(function(){
                    // this.$session.destroy()
                    this.$cookies.remove('Admin-Token-Otp')
                    this.$cookies.remove('Admin-Token')
                    // this.$router.push('/login')
                }, 3000);
                setTimeout(function(){
                    notify()
                        .then(res => {
                            console.log(res.data.status)
                            // this.loading = true
                        })
                }, 7000);
            }
        },
        watch: {
            'dem'() {
                this.$store.dispatch('LogOut')
                console.log('dmđm')
                this.$router.push('/confirm')
            }
        }
    }
</script>

<style scoped>

</style>
