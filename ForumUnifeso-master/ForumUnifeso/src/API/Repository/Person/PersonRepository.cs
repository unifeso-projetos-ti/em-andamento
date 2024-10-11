using ForumUnifeso.src.API.Base;
using ForumUnifeso.src.API.Base.Context;
using ForumUnifeso.src.API.Interface;
using ForumUnifeso.src.API.Model;
using Microsoft.EntityFrameworkCore;
using System;

namespace ForumUnifeso.src.API.Repository
{
    public class PersonRepository : IPersonRepository
    {
        private readonly PrincipalDbContext _context;

        public PersonRepository(PrincipalDbContext context)
        {
            _context = context;
        }

        public async Task<Person> AddAsync(Person person)
        {
            _context.Person.Add(person);
            await _context.SaveChangesAsync();
            return person;
        }

        public async Task<Person> UpdateAsync(Person person)
        {
            _context.Person.Update(person);
            await _context.SaveChangesAsync();
            return person;
        }

        public async Task<Person?> GetByIdAsync(int personId)
        {
            return await _context.Person.FirstOrDefaultAsync(person => person.Id == personId);
        }

        public async Task<IEnumerable<Person>> GetAllAsync()
        {
            return await _context.Person.ToListAsync();
        }

        public async Task<bool> DeleteByIdAsync(int id)
        {
            var person = await GetByIdAsync(id);
            if (person is not null)
            {
                _context.Person.Remove(person);
                await _context.SaveChangesAsync();
                return true;
            }
            else
            {
                return false;
            }
        }

        public async Task<bool> DeleteAsync(Person person)
        {
            _context.Person.Remove(person);
            await _context.SaveChangesAsync();
            return true;
        }

    }
}
