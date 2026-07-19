class ImportGraph:

    def build(self, modules):

        forward = {}
        reverse = {}

        module_names = {}

        for module in modules:

            name = (
                module.path
                .replace("\\", "/")
                .replace("/", ".")
                .replace(".py", "")
            )

            module_names[name] = module.path

        for module in modules:

            deps = []

            for imp in module.imports:

                if imp in module_names:
                    deps.append(module_names[imp])

            forward[module.path] = sorted(set(deps))

        for module in forward:

            reverse.setdefault(module, [])

        for module, deps in forward.items():

            for dep in deps:
                reverse.setdefault(dep, []).append(module)

        reverse = {
            k: sorted(set(v))
            for k, v in reverse.items()
        }

        isolated = sorted(
            module
            for module in forward
            if not forward[module]
            and not reverse.get(module)
        )

        cycles = []

        visited = set()

        def dfs(node, stack):

            if node in stack:
                idx = stack.index(node)
                cycles.append(stack[idx:] + [node])
                return

            if node in visited:
                return

            visited.add(node)

            for dep in forward.get(node, []):
                dfs(dep, stack + [node])

        for module in forward:
            dfs(module, [])

        memo = {}

        def depth(node):

            if node in memo:
                return memo[node]

            deps = forward.get(node, [])

            if not deps:
                memo[node] = 0
                return 0

            memo[node] = 1 + max(
                depth(dep)
                for dep in deps
            )

            return memo[node]

        depths = {
            module: depth(module)
            for module in forward
        }

        return {
            "imports": forward,
            "reverse": reverse,
            "isolated": isolated,
            "cycles": cycles,
            "depth": depths,
        }


imports = ImportGraph()
