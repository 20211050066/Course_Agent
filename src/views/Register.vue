<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 24px; margin-bottom: 20px">欢迎注册</h1>
      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item>
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入用户名"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item>
          <el-input
            type="password"
            size="large"
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <el-form-item>
          <el-input
            type="password"
            size="large"
            v-model="form.confirmPassword"
            placeholder="请确认密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <div>
          <el-button type="primary" size="large" style="width: 100%">注册</el-button>
          <div style="text-align: right; margin-top: 12px">
            已有账号？请<a href="/login" style="color: var(--el-color-primary)">登录</a>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'

const form = reactive({
  username: '',
  password: '',
  confirmPassword: ''
})
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
  background-color: white;
}
</style>
