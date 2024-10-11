import { nextui } from '@nextui-org/react'
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    './node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}',
  ],
  darkMode: ['class'],
  theme: {
    extend: {
      height: {
        heightLessNav: 'h-[calc(100vh-64px)]',
      },
      screens: {
        smphoneMax: { max: '320px' },
        bigphoneMax: { max: '500px' },
        smMax: { max: '640px' },
        mdMax: { max: '768px' },
        lgMax: { max: '1024px' },
      },
      maxWidth: {
        '8xl': '1440px',
      },
      colors: {
        'text-color': '#000000',
        'main-color': '#302b2b',
        'primary-bg': '#fff',
        'secondary-bg': '#e9e9e9',
        dark: {
          background: '#262626',
          text: '#ffffff',

          // Navbar Variables Dark
          'background-navigation-bar': '#262626',
          'background-activate-route': '#171717',
          'icon-color': '#ffffff',
          'border-color-navigation': '#404040',
        },
        light: {
          background: '#fff',
          text: '#000',

          // Navbar Variables Light
          'background-navigation-bar': '#fff',
          'background-activate-route': '#e2e8f0',
          'icon-color': '#000000',
          'border-color-navigation': '#f1f5f9',
        },
      },
    },
  },
  plugins: [nextui()],
}
export default config
