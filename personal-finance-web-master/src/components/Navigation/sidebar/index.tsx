'use client'

import { IconMenu2, IconX } from '@tabler/icons-react'
import { AnimatePresence, motion } from 'framer-motion'
import Link, { LinkProps } from 'next/link'
import { usePathname } from 'next/navigation'
import React, { createContext, useContext, useState } from 'react'
import { cn } from 'src/utils/cn'
import { IRoutes } from '..'

// Sidebar Context and Provider
interface Links {
  label: string
  href: string
  icon: React.ReactNode
}

interface SidebarContextProps {
  open: boolean
  setOpen: React.Dispatch<React.SetStateAction<boolean>>
  animate: boolean
}

const SidebarContext = createContext<SidebarContextProps | undefined>(undefined)

export const useSidebar = () => {
  const context = useContext(SidebarContext)
  if (!context) {
    throw new Error('useSidebar must be used within a SidebarProvider')
  }
  return context
}

export const SidebarProvider = ({
  children,
  open: openProp,
  setOpen: setOpenProp,
  animate = true,
}: {
  children: React.ReactNode
  open?: boolean
  setOpen?: React.Dispatch<React.SetStateAction<boolean>>
  animate?: boolean
}) => {
  const [openState, setOpenState] = useState(false)

  const open = openProp !== undefined ? openProp : openState
  const setOpen = setOpenProp !== undefined ? setOpenProp : setOpenState

  return (
    <SidebarContext.Provider value={{ open, setOpen, animate }}>
      {children}
    </SidebarContext.Provider>
  )
}

// Sidebar Components
export const Sidebar = ({
  children,
  open,
  setOpen,
  animate,
}: {
  children: React.ReactNode
  open?: boolean
  setOpen?: React.Dispatch<React.SetStateAction<boolean>>
  animate?: boolean
}) => {
  return (
    <SidebarProvider open={open} setOpen={setOpen} animate={animate}>
      {children}
    </SidebarProvider>
  )
}

export const SidebarBody = (props: React.ComponentProps<typeof motion.div>) => {
  return (
    <>
      <DesktopSidebar {...props} />
      <MobileSidebar {...(props as React.ComponentProps<'div'>)} />
    </>
  )
}

export const DesktopSidebar = ({
  className,
  children,
  ...props
}: React.ComponentProps<typeof motion.div>) => {
  const { open, setOpen, animate } = useSidebar()
  return (
    <motion.div
      className={cn(
        'px-4 py-4 h-full hidden md:flex md:flex-col dark:bg-dark-background-navigation-bar bg-light-background-navigation-bar w-[300px] flex-shrink-0',
        className
      )}
      animate={{
        width: animate ? (open ? '300px' : '80px') : '300px',
      }}
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
      {...props}
    >
      {children}
    </motion.div>
  )
}

export const MobileSidebar = ({
  className,
  children,
  ...props
}: React.ComponentProps<'div'>) => {
  const { open, setOpen } = useSidebar()
  return (
    <div
      className={cn(
        'h-10 px-4 py-4 flex flex-row md:hidden items-center justify-between dark:bg-dark-background-navigation-bar bg-light-background-navigation-bar w-full ',
        className
      )}
      {...props}
    >
      <div className="flex justify-end z-20 w-full ">
        <IconMenu2
          className="dark:text-dark-text text-light-text"
          onClick={() => setOpen(!open)}
        />
      </div>
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ x: '-100%', opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: '-100%', opacity: 0 }}
            transition={{
              duration: 0.3,
              ease: 'easeInOut',
            }}
            className={cn(
              'fixed h-full w-full inset-0 bg-light-background-navigation-bar dark:bg-dark-background-navigation-bar p-10 z-[100] flex flex-col justify-between',
              className
            )}
          >
            <div
              className="absolute right-10 top-10 z-50 text-light-text dark:text-dark-text"
              onClick={() => setOpen(!open)}
            >
              <IconX />
            </div>
            {children}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

export const SidebarLink = ({
  link,
  className,
  ...props
}: {
  link: IRoutes
  className?: string
  props?: LinkProps
}) => {
  const pathname = usePathname()
  const isActive = pathname === link.router
  const { open, animate } = useSidebar()

  return (
    <Link
      href={link.router}
      className={cn(
        'flex items-center justify-start gap-2 group/sidebar p-2 capitalize ',
        isActive && !open
          ? 'dark:bg-dark-background-activate-route bg-light-background-activate-route rounded-md w-fit'
          : '',
        isActive && open
          ? 'dark:bg-dark-background-activate-route bg-light-background-activate-route p-2 rounded-lg dark:text-dark-text text-light-text font-bold'
          : '',
        className
      )}
      {...props}
    >
      {link.icon}
      <motion.span
        animate={{
          display: animate ? (open ? 'inline-block' : 'none') : 'inline-block',
          opacity: animate ? (open ? 1 : 0) : 1,
        }}
        className="dark:text-dark-text text-light-text text-sm group-hover/sidebar:translate-x-1 transition duration-150 whitespace-pre inline-block !p-0 !m-0"
      >
        {link.name}
      </motion.span>
    </Link>
  )
}

export const Logo = () => {
  return (
    <Link
      href="#"
      className="font-normal flex space-x-2 items-center text-sm dark:text-dark-text text-light-text py-1  relative z-20"
    >
      <div className="h-5 w-6 dark:bg-dark-text bg-light-text rounded-br-lg rounded-tr-sm rounded-tl-lg rounded-bl-sm flex-shrink-0" />
      <motion.span
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="font-medium dark:text-dark-text text-light-text whitespace-pre"
      >
        Acet Labs
      </motion.span>
    </Link>
  )
}
export const LogoIcon = () => {
  return (
    <Link
      href="#"
      className="font-normal flex space-x-2 items-center text-sm dark:text-dark-text text-light-text py-1 relative z-20"
    >
      <div className="h-5 w-6 dark:bg-dark-text bg-light-text rounded-br-lg rounded-tr-sm rounded-tl-lg rounded-bl-sm flex-shrink-0" />
    </Link>
  )
}
