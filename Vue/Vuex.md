[toc]

## 基础设置

### 创建项目

```bash
npm config set registry https://registry.npm.taobao.org #更改为taobao家的镜像

npm install -g @vue/cli # 全局安装vue/cli

vue create practice-vuex # 创建vue项目，并命名为practice-vuex
```

### 禁用eslint语法检查器

在vue.config.js中

```js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false
})
```

## 入门案例（加减法）

### 安装和引入 Vuex

首先，确保你已经安装了 Vuex。

```bash
npm install vuex@next --save  # 对于 Vue 3 使用 @next 标签
```

在项目中创建一个 `store` 文件夹，并在其中创建 `index.js` 文件。

###  创建 Store

在 `store/index.js` 中初始化 Vuex store。

```javascript
// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    count: 0 // 初始计数
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    decrement(state) {
      state.count--;
    }
  }
});
```

### 在 Vue 应用中使用 Store

在 `main.js` 或 `app.js` 中引入并使用 store。

```javascript
import { createApp } from 'vue';
import App from './App.vue';
import store from './store';

createApp(App).use(store).mount('#app');
```

### Home视图

```vue
<!--views\Home.vue-->
<template>
    <div>
      <h1>Count: {{ count }}</h1>
      <Add />
      <Sub />
    </div>
  </template>
  
  <script>
  import Add from '../components/Add.vue';
  import Sub from '../components/Sub.vue';
  
  export default {
    name: 'Home',
    components: {
      Add,
      Sub
    },
    computed: {
      count() {
        return this.$store.state.count;
      }
    }
  };
  </script>
```

### Add组件

```vue
<!-- Add.vue -->
<template>
    <div>
      <button @click="increment">+</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Add',
    methods: {
      increment() {
        this.$store.commit('increment');
      }
    }
  };
  </script>
```

### Sub组件

```vue
<!-- Sub.vue -->
<template>
<div>
    <button @click="decrement">-</button>
</div>
</template>

<script>
    export default {
        name: 'Sub',
        methods: {
            decrement() {
                this.$store.commit('decrement');
            }
        }
    };
</script>
```



## 扩展

### 持久化

页面刷新时，数据依然在，而不是一刷新就没了

```js
// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    count: Number(localStorage.getItem('count')) || 0 // 初始化时从localStorage读取count值
  },
  mutations: {
    increment(state) {
      state.count++;
      localStorage.setItem('count', state.count); // 更新localStorage中的count值
    },
    decrement(state) {
      state.count--;
      localStorage.setItem('count', state.count); // 更新localStorage中的count值
    }
  }
});
```



### 模拟监听

```js
<!-- Add.vue -->
<template>
    <div>
      <button @click="increment">+</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Add',
    methods: {
      increment() {
        this.$store.commit('increment');
        this.$store.dispatch('checkAndTrigger');//检查是否达到触发条件
      }
    }
  };
  </script>
```



```js
// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    count: Number(localStorage.getItem('count')) || 0 // 初始化时从localStorage读取count值
  },
  mutations: {
    increment(state) {
      state.count++;
      localStorage.setItem('count', state.count); // 更新localStorage中的count值
    },
    decrement(state) {
      state.count--;
      localStorage.setItem('count', state.count); // 更新localStorage中的count值
    }
  },
  getters: {
    // 计算属性：判断是否达到了触发条件
    isCountFive: (state) => {
      return state.count === 5;
    }
  },
  actions: {
    // 触发特定条件时的操作
    checkAndTrigger({ state, getters, commit }) {
      if (getters.isCountFive) {
        // 这里可以放你想要触发的操作，比如打印一条消息或调用一个函数
        alert('Count has reached 5! Performing the trigger action...');
        // 你也可以在这里触发其他的 mutation 或 action
        // commit('someMutation');
      }
    }
  }
});
```

