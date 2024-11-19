local builtin = require('telescope.builtin')
require("telescope").load_extension("flutter")
-- require('telescope.builtin').diagnostics({ severity_bound = 0 })

-- vim.keymap.set('n', '<leader>pf', builtin.find_files, {})
vim.keymap.set('n', '<C-p>', builtin.git_files, {})
vim.keymap.set('n', '<leader>ps', function()
    builtin.grep_string({ search = vim.fn.input("Grep > ") });
end)

vim.api.nvim_set_keymap('n', '<leader>pf',
    '<cmd>Telescope find_files find_command=fd, prompt_prefix=🔍 <CR>',
    {
        noremap = true,
        silent = true
    })
vim.api.nvim_set_keymap('n', '<leader>dd', '<cmd>Telescope diagnostics severity_bound=ERROR<CR>',
    { noremap = true, silent = true })
