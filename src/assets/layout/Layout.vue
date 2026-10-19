<template>
  <el-container style="min-height: 100vh">
    <!-- 第一部分：顶部导航栏 -->
    <el-header
      style="
        align-items: center;
        height: 60px;
        display: flex;
        border-bottom: 1px solid #ddd;
        background-color: #fff;
      "
    >
      <div style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold">
        🧪
        <div style="margin-left: 5px">智能实验室预约系统</div>
      </div>
      <div>
        <el-dropdown>
          <div style="display: flex; align-items: center; cursor: pointer">
            <el-avatar :size="40">管</el-avatar>
            <span style="margin-left: 5px">管理员</span>
          </div>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
              <el-dropdown-item>Action 2</el-dropdown-item>
              <el-dropdown-item>Action 3</el-dropdown-item>
              <el-dropdown-item disabled>Action 4</el-dropdown-item>
              <el-dropdown-item divided>Action 5</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </el-header>

    <el-container class="layout-body">
      <!-- 第二部分：左侧菜单栏 -->
      <el-aside width="220px" class="layout-aside">
        <el-menu router style="height: 100%" default-active="/layout/home">
          <el-menu-item index="/layout/home">
            <el-icon><icon-menu /></el-icon>
            <span>系统首页</span>
          </el-menu-item>
          <el-menu-item index="/layout/lab">
            <el-icon><House /></el-icon>
            <span>实验室管理</span>
          </el-menu-item>
          <el-menu-item index="/layout/device">
            <el-icon><Setting /></el-icon>
            <span>设备列表管理</span>
          </el-menu-item>
          <el-menu-item index="/layout/user">
            <el-icon><User /></el-icon>
            <span>用户管理</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 第三部分：主内容区 -->
      <el-main class="layout-main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { House, Menu as IconMenu, Setting, User } from '@element-plus/icons-vue'
import router from '@/router'
const logout = () => {
  // 退出登录逻辑
  router.push('/login')
}
</script>
