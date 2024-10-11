'use client'

import { DatePicker, DatePickerProps } from '@nextui-org/date-picker'
import { Control, Controller } from 'react-hook-form'

export type FormInputProps = {
  name: string
  control: Control<any, any>
} & DatePickerProps

export default function DatePickerComponent({
  name,
  ...props
}: FormInputProps) {
  return (
    <>
      <Controller
        control={props.control}
        name="date"
        rules={{ required: true }}
        render={({ field, formState }) => {
          return (
            <DatePicker
              {...props}
              value={field.value}
              isInvalid={!!formState.errors?.[name]?.message}
              errorMessage={formState.errors?.[name]?.message?.toString()}
              onChange={(date) => {
                field.onChange(date)
              }}
            />
          )
        }}
      />
    </>
  )
}
