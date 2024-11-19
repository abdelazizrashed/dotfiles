local ls = require("luasnip")
local s = ls.snippet
-- local sn = ls.snippet_node
-- local isn = ls.indent_snippet_node
local t = ls.text_node
local i = ls.insert_node
-- local f = ls.function_node
-- local c = ls.choice_node
-- local d = ls.dynamic_node
-- local r = ls.restore_node
-- local events = require("luasnip.util.events")
-- local ai = require("luasnip.nodes.absolute_indexer")
-- local extras = require("luasnip.extras")
-- local l = extras.lambda
-- local rep = extras.rep
-- local p = extras.partial
-- local m = extras.match
-- local n = extras.nonempty
-- local dl = extras.dynamic_lambda
-- local fmt = require("luasnip.extras.fmt").fmt
-- local fmta = require("luasnip.extras.fmt").fmta
-- local conds = require("luasnip.extras.expand_conditions")
-- local postfix = require("luasnip.extras.postfix").postfix
-- local types = require("luasnip.util.types")
-- local parse = require("luasnip.util.parser").parse_snippet
-- local ms = ls.multi_snippet
-- local k = require("luasnip.nodes.key_indexer").new_key
--

ls.filetype_extend("javascript", { "javascriptreact" })
ls.filetype_extend("javascript", { "html" })


-- Keybinding for jumping forward in a snippet with <C-Tab>
vim.keymap.set({ "i", "s" }, "<C-s>", function()
    if ls.jumpable(1) then
        ls.jump(1)
    end
end, { silent = true })

-- Keybinding for jumping backward in a snippet with <C-S-Tab> (Control + Shift + Tab)
vim.keymap.set({ "i", "s" }, "<C-S-s>", function()
    if ls.jumpable(-1) then
        ls.jump(-1)
    end
end, { silent = true })

local function get_current_date()
    return os.date("%Y/%m/%d")
end

ls.add_snippets("all", {
    s("todo", {
        t("// TODO (abdelaziz): "), i(1, "todo"),
    }),
    -- s("sign", {
    --     t("// Auther: Abdelaziz Rashed @ 2024/"), i(1, "m"), t("/"), i(2, "d"),
    -- }),
    s("sign", {
        t("// Author: Abdelaziz Rashed @ "), t(get_current_date()),
    }),
    ls.parser.parse_snippet({ trig = "lsp" },
        "class ${1:name}Loading extends ${1:name}State {}"),
})
ls.add_snippets("dart", {
    ls.parser.parse_snippet({ trig = "blocexcute" },
        [[emit(${1:name}Loading());
await excuteBlocAndHandleError(
  execute: () async {
    final model = await _repository.${2:function}(
      onError: (msg) => emit(${1:name}Error(msg)),
    );
    if (!model.success) return;
    emit(${1:name}Loaded(model.data!));
  },
  onError: (msg) => emit(${1:name}Error(msg)),
  onNetwork: (msg) => emit(${1:name}NetworkConnectionError(msg)),
);]]
    ),
    ls.parser.parse_snippet({ trig = "blocinit" },
        [[

part '';
part '';

class ${1:name}Bloc extends Bloc<${1:name}Event, ${1:name}State> {
    static ${1:name}Bloc of(BuildContext context) =>
        BlocProvider.of<${1:name}Bloc>(context);

    final ${1:name}Repository _repository;

    ${1:name}Bloc({
      required ${1:name}Repository repository,
    })  : _repository = repository,
          super(${1:name}Initial()) {
      on<${2:event}>(_on${2:event});
    }
}
        ]]
    ),
ls.parser.parse_snippet({trig = "platview"},
    [[
import 'package:flutter/material.dart';

class ${1:name}Screen extends StatelessWidget {
  static const routeName = "/${2:lower_name}";

  static final route = ModuleRoute(
    routeName: routeName,
    builder: (_, __) => const ${1:name}Screen(),
  );
  const ${1:name}Screen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text("${1:name}Screen"),
      ),
    );
  }
}
        
    ]]),
    ls.parser.parse_snippet({ trig = "blocprovide" },
        [[
BlocProvider(
  create: (_) => ${1:name}Bloc(
    repository: ${1:name}Repository.of(context),
  ),
),
        ]]
    ),
    ls.parser.parse_snippet({ trig = "blocstate" },
        [[
part of '${2:lower_name}_bloc.dart';

abstract class ${1:name}State extends Equatable {
  const ${1:name}State();

  @override
  List<Object> get props => [];
}

class ${1:name}Initial extends ${1:name}State {}
class ${1:name}Loading extends ${1:name}State {}

class ${1:name}Loaded extends ${1:name}State {
  final ${1:name}Model data;

  const ${1:name}Loaded(this.data);

  @override
  List<Object> get props => [data];
}

class ${1:name}Error extends ${1:name}State {
  final String message;

  const ${1:name}Error(this.message);

  @override
  List<Object> get props => [message];
}

class ${1:name}NetworkConnectionError extends ${1:name}State {
  final String message;

  const ${1:name}NetworkConnectionError(this.message);

  @override
  List<Object> get props => [message];
}

        ]]
    ),
    ls.parser.parse_snippet({ trig = "blocevent" },
        [[
part of '${2:lower_name}_bloc.dart';

abstract class ${1:name}Event extends Equatable {
  const ${1:name}Event();

  @override
  List<Object> get props => [];
}

        ]]
    ),
    ls.parser.parse_snippet({ trig = "blocstatesuccess" },
        [[

part of '${2:lower_name}_bloc.dart';

abstract class ${1:name}State extends Equatable {
  const ${1:name}State();

  @override
  List<Object> get props => [];
}

class ${1:name}Initial extends ${1:name}State {}
class ${1:name}Loading extends ${1:name}State {}

class ${1:name}Success extends ${1:name}State {
  final String msg;

  const ${1:name}Success(this.msg);

  @override
  List<Object> get props => [msg];
}

class ${1:name}Error extends ${1:name}State {
  final String message;

  const ${1:name}Error(this.message);

  @override
  List<Object> get props => [message];
}

class ${1:name}NetworkConnectionError extends ${1:name}State {
  final String message;

  const ${1:name}NetworkConnectionError(this.message);

  @override
  List<Object> get props => [message];
}

        ]]
    ),
    ls.parser.parse_snippet({ trig = "repoabs" },
        [[
abstract class ${1:repo}Repository {
  static ${1:repo}Repository of(BuildContext context) =>
      RepositoryProvider.of<${1:repo}Repository>(context);

  static ${1:repo}Repository create() => ${1:repo}RepositoryImpl();
}
        ]]
    ),
    ls.parser.parse_snippet({ trig = "repoimpl" },
        [[
class ${1:repo}RepositoryImpl implements ${1:repo}Repository{}
        ]]
    ),
    ls.parser.parse_snippet({ trig = "repoprovide" },
        [[
RepositoryProvider(create: (_) => ${1:name}Repository.create()),
        ]]
    ),
    ls.parser.parse_snippet({
        trig = "nblocinitrepo",
        dscr = "Creates a Bloc class with repository",
    }, [[

part '${2:lower_name}_state.dart';
part '${2:lower_name}_event.dart';

class ${1:name}Bloc extends Bloc<${1:name}Event, ${1:name}State> {
    static final dependency = BlocDependency<${1:name}Bloc>(
    factory: () => ${1:name}Bloc(),
    );

    /// Get instance of [${1:name}Bloc] using ServiceLocator
    static ${1:name}Bloc get instance => dependency.get();

    /// Alias for [${1:name}Bloc.instance]
    /// Get instance of [${1:name}Bloc] using ServiceLocator
    static ${1:name}Bloc get i => dependency.get();

    /// Get instance of [${1:name}Bloc] using InheritedWidget
    static ${1:name}Bloc of(BuildContext context) =>
      BlocProvider.of<${1:name}Bloc>(context);

    final ${1:name}Repository _repository;

    ${1:name}Bloc({
      required ${1:name}Repository repository,
    })  : _repository = repository,
          super(${1:name}Initial()) {
      on<${3:event}>(_on${3:event});
    }
}
]]),
    ls.parser.parse_snippet({ trig = "singleton" }, [[
  static ${1:name}? _instance;
  static ${1:name} get instance => _instance ??= ${1:name}._();
  static ${1:name} get i => _instance ??= ${1:name}._();

  ${1:name}._();

]]),
    ls.parser.parse_snippet({ trig = "dataclass" }, [[
import 'package:json_annotation/json_annotation.dart';

part '${2:lower_name}.g.dart';

@JsonSerializable(fieldRename: FieldRename.snake)
class ${1:name} {
  ${3:fields}

  ${1:name}({
  });

  factory ${1:name}.fromJson(Map<String, dynamic> json) =>
      _$${1:name}FromJson(json);

  Map<String, dynamic> toJson() => _$${1:name}ToJson(this);
}

]]),
    ls.parser.parse_snippet({
            trig = "nblocinit",
            dscr = "Creates a Bloc class without repository",
        },
        [[

part '${2:lower_name}_state.dart';
part '${2:lower_name}_event.dart';

class ${1:name}Bloc extends Bloc<${1:name}Event, ${1:name}State> {
    static final dependency = BlocDependency<${1:name}Bloc>(
    factory: () => ${1:name}Bloc(),
    );

    /// Get instance of [${1:name}Bloc] using ServiceLocator
    static ${1:name}Bloc get instance => dependency.get();

    /// Alias for [${1:name}Bloc.instance]
    /// Get instance of [${1:name}Bloc] using ServiceLocator
    static ${1:name}Bloc get i => dependency.get();

    /// Get instance of [${1:name}Bloc] using InheritedWidget
    static ${1:name}Bloc of(BuildContext context) =>
      BlocProvider.of<${1:name}Bloc>(context);


    ${1:name}Bloc(): super(${1:name}Initial()) {
      on<${3:event}>(_on${3:event});
    }
}
]])
    -- ls.parser.parse_snippet({ trig = "" },
    --     [[
    --
    --     ]]
    -- ),
    -- ls.parser.parse_snippet({ trig = "" },
    --     [[
    --
    --     ]]
    -- ),
})
