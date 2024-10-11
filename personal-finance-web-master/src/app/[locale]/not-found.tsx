'use client'
import { useTranslations } from 'next-intl'

export default function NotFound() {
  const t = useTranslations('NotFound')
  return (
    <div className="h-screen w-full dark:bg-dark-background  bg-light-background">
      <header className="flex justify-center items-center dark:text-dark-text text-light-text">
        <h1>{t('title')}</h1>
      </header>
    </div>
  )
}
